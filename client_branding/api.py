import frappe

@frappe.whitelist()
def get_branding():
    """
    Returns branding settings for the logged-in user's default company.
    Safe for Frappe Cloud. No client-side company input accepted.
    """

    user = frappe.session.user
    if user == "Guest":
        return {}

    user_doc = frappe.get_doc("User", user)
    company = user_doc.default_company

    if not company:
        return {}

    company_doc = frappe.get_doc("Company", company)

    # Use getattr defensively so missing fields never crash
    return {
        "company": company,
        "logo": getattr(company_doc, "custom_brand_logo", None),
        "primary_color": getattr(company_doc, "custom_brand_primary_color", None),
        "secondary_color": getattr(company_doc, "custom_brand_secondary_color", None),
        "favicon": getattr(company_doc, "custom_brand_favicon", None),
        "custom_css": getattr(company_doc, "custom_brand_css", None),
    }
