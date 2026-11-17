# ShieldLog data model

## Entity overview

```
┌──────────────────────────────┐
│           Finding            │
├──────────────────────────────┤
│ id           INTEGER (PK)    │
│ title        STRING(200)     │
│ description  TEXT            │
│ category     STRING(50)      │
│ severity     STRING(20)      │
│ status       STRING(30)      │
│ created_at   DATETIME        │
│ updated_at   DATETIME        │
└──────────────────────────────┘
```

Single-entity model on purpose. Course demo stays small and easy to verify.

## Field rules

| Field | Allowed values |
|-------|----------------|
| `category` | `phishing`, `malware`, `misconfig`, `access`, `other` |
| `severity` | `low`, `medium`, `high`, `critical` |
| `status` | `open`, `investigating`, `resolved` |

## Relationships
- No foreign keys in v1.
- Future (not implemented): `Asset` 1—* `Finding`, `User` 1—* `Finding` for ownership.

## Why this model
Security teams often start with a lightweight intake queue before a full ticketing system. Title + category + severity + status covers the minimum workflow: report → triage → resolve.
