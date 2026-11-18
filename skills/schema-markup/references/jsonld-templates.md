# JSON-LD Templates

## Organization + WebSite
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Inc.",
      "url": "https://example.com/",
      "logo": "https://example.com/logo.png",
      "sameAs": ["https://www.linkedin.com/company/example", "https://x.com/example"]
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com/",
      "name": "Example",
      "publisher": { "@id": "https://example.com/#organization" }
    }
  ]
}
```

## BlogPosting + FAQPage
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "headline": "How to Build a B2B Lead Scoring Model",
      "datePublished": "2026-11-01",
      "dateModified": "2026-11-15",
      "image": "https://example.com/img/b2b-lead-scoring-model.png",
      "author": { "@type": "Person", "name": "Jane Doe", "url": "https://example.com/authors/jane-doe" },
      "publisher": { "@id": "https://example.com/#organization" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "What is lead scoring?",
        "acceptedAnswer": { "@type": "Answer", "text": "Lead scoring ranks leads by fit and engagement so sales works the best ones first." }
      }]
    }
  ]
}
```

## SoftwareApplication
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Example",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "offers": { "@type": "Offer", "price": "49", "priceCurrency": "USD" }
}
```
