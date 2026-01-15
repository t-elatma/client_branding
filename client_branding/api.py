import frappe

@frappe.whitelist()
def get_branding():
    """
    Returns branding for the logged-in user's default company.
    Works on Frappe Cloud and modern ERPNext versions.
    """

    if frappe.session.user == "Guest":
        return {}

    # ✅ Correct way to get default company
    company = frappe.defaults.get_user_default("Company")

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
