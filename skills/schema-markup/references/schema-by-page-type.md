# Schema by Page Type

| Page | Schema |
|---|---|
| Homepage | Organization (logo, sameAs social profiles, contactPoint), WebSite (with SearchAction if site search exists) |
| Blog post | BlogPosting/Article (headline, author → Person, datePublished, dateModified, image, publisher → Organization), BreadcrumbList, FAQPage if visible FAQs |
| Product (SaaS) | SoftwareApplication or Product (name, applicationCategory, offers, aggregateRating only from real reviews) |
| Pricing | Product/SoftwareApplication with multiple Offer nodes |
| Webinar/event | Event (eventAttendanceMode Online/Offline, location VirtualLocation, startDate, organizer, offers) |
| Video page | VideoObject (name, description, thumbnailUrl, uploadDate, duration, contentUrl/embedUrl) |
| Author page | Person (name, jobTitle, worksFor, sameAs LinkedIn) |
| Local office | LocalBusiness/ProfessionalService (address, geo, openingHours) |
| Case study | Article + about → Organization (customer) |
