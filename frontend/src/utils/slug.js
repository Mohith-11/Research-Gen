/**
 * Converts a heading string into a URL-friendly anchor ID.
 * Must match exactly between markdown-it renderer (ReportViewer)
 * and the TOC parser (TableOfContents) so IntersectionObserver links up.
 */
export function slugify(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")   // strip special chars
    .replace(/\s+/g, "-")        // spaces → hyphens
    .replace(/-+/g, "-");        // collapse multiple hyphens
}
