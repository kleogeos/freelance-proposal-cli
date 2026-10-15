#!/usr/bin/env python3
"""Generate a clean HTML client proposal/quote from a JSON file. Zero dependencies."""
import argparse
import html
import json
import sys


def money(n):
    return f"${n:,.2f}"


def render(data):
    pricing = data["pricing"]
    total = sum(p["amount"] for p in pricing)

    scope_items = "\n".join(
        f"<li>{html.escape(s)}</li>" for s in data.get("scope", [])
    )

    pricing_rows = "\n".join(
        f"<tr><td>{html.escape(p['description'])}</td>"
        f"<td style='text-align:right'>{money(p['amount'])}</td></tr>"
        for p in pricing
    )

    summary = html.escape(data.get("summary", ""))
    timeline = html.escape(data.get("timeline", ""))
    terms = html.escape(data.get("terms", ""))
    notes = html.escape(data.get("notes", ""))

    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Proposal {html.escape(data.get('proposal_number', ''))}</title>
<style>
body{{font-family:-apple-system,Arial,sans-serif;max-width:680px;margin:40px auto;color:#1a1a1a}}
table{{width:100%;border-collapse:collapse;margin-top:12px}}
th,td{{padding:8px;border-bottom:1px solid #ddd}}
th{{text-align:left;color:#666;font-size:13px;text-transform:uppercase}}
.total{{font-size:20px;font-weight:bold}}
.meta{{color:#666;font-size:14px}}
h2{{font-size:15px;text-transform:uppercase;color:#666;margin-top:28px;margin-bottom:4px}}
ul{{margin-top:4px}}
.sign{{margin-top:48px;display:flex;gap:40px}}
.sign div{{flex:1;border-top:1px solid #333;padding-top:4px;font-size:13px;color:#666}}
@media print{{body{{margin:0}}}}
</style></head><body>
<h1>Proposal {html.escape(data.get('proposal_number', ''))}</h1>
<p class="meta">From: {html.escape(data.get('from', ''))}<br>
To: {html.escape(data.get('to', ''))}<br>
Date: {html.escape(data.get('date', ''))} &middot; Valid until: {html.escape(data.get('valid_until', ''))}</p>

{"<h2>Summary</h2><p>" + summary + "</p>" if summary else ""}
{"<h2>Scope of work</h2><ul>" + scope_items + "</ul>" if scope_items else ""}

<h2>Pricing</h2>
<table>
<tr><th>Item</th><th style="text-align:right">Amount</th></tr>
{pricing_rows}
</table>
<p style="text-align:right;margin-top:8px"><span class="total">Total: {money(total)}</span></p>

{"<h2>Timeline</h2><p>" + timeline + "</p>" if timeline else ""}
{"<h2>Terms</h2><p>" + terms + "</p>" if terms else ""}
{"<p class='meta'>" + notes + "</p>" if notes else ""}

<div class="sign">
<div>Accepted by (client), date</div>
<div>{html.escape(data.get('from', ''))}, date</div>
</div>
</body></html>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", help="JSON proposal file (see example.json)")
    ap.add_argument("-o", "--output", help="output HTML file (default: stdout)")
    args = ap.parse_args()

    try:
        with open(args.input) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in {args.input}: {e}", file=sys.stderr)
        sys.exit(1)

    if "pricing" not in data or not data["pricing"]:
        print("Error: JSON must include a non-empty 'pricing' list", file=sys.stderr)
        sys.exit(1)

    out = render(data)
    if args.output:
        with open(args.output, "w") as f:
            f.write(out)
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
