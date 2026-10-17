# freelance-proposal-cli

![Test CLI](https://github.com/kleogeos/freelance-proposal-cli/actions/workflows/test.yml/badge.svg)
Generate a clean, print-ready HTML client proposal/quote from a JSON file. No dependencies, no sign-up, no SaaS account — just a file you can commit, version, and send as a link or PDF.

```bash
python3 proposal.py example.json -o proposal.html
```

Produces a one-page proposal: summary, scope of work, itemized pricing with a total, timeline, terms, and a signature line — ready to open in a browser and print to PDF or send as a link.

### Install (optional)

```bash
pip install git+https://github.com/kleogeos/freelance-proposal-cli
freelance-proposal example.json -o proposal.html
```

### JSON format

```json
{
  "proposal_number": "P-2026-014",
  "from": "Your name",
  "to": "Client name",
  "date": "2026-10-15",
  "valid_until": "2026-11-15",
  "summary": "One-paragraph description of the project.",
  "scope": ["Task one", "Task two"],
  "pricing": [{"description": "Design", "amount": 1800}],
  "timeline": "4 weeks from signed proposal.",
  "terms": "50% deposit to start, 50% on delivery.",
  "notes": "Optional free-text note."
}
```

Only `pricing` is required; every other field is optional and omitted sections just don't render.

### Where this fits

Proposal gets accepted → track the work with [freelance-time-cli](https://github.com/kleogeos/freelance-time-cli) → log costs with [freelance-expense-cli](https://github.com/kleogeos/freelance-expense-cli) → turn the hours into an invoice with [freelance-timesheet-to-invoice-cli](https://github.com/kleogeos/freelance-timesheet-to-invoice-cli) → render it with [freelance-invoice-cli](https://github.com/kleogeos/freelance-invoice-cli). Same zero-dependency, local-file philosophy across all five.

Free web tools (no install): [invoice generator](https://kleogeos.github.io/freelancer-tools/invoice.html) · [rate calculator](https://kleogeos.github.io/freelancer-tools/rate-calculator.html) · [contract checklist](https://kleogeos.github.io/freelancer-tools/contract-checklist.html)

Need the paperwork beyond this one tool — contracts, invoices, late-payment emails, client scripts? [Freelancer Starter Kit ($15, crypto or Telegram Stars, no KYC)](https://kleogeos.github.io/freelancer-tools/kit.html?src=cli-proposal)

Free and will stay free. If it saved you time: [tip with crypto](https://kleogeos.github.io/freelancer-tools/donate.html).

## License

MIT — do whatever you want with it.
