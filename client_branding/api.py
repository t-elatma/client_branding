import frappe

@frappe.whitelist()
def get_branding():
    """
    Returns branding for the logged-in user's default company.
    Returns empty dict if no company is found or accessible.
    """

    user = frappe.session.user
    if user == "Guest":
        return {}

    # 1️⃣ Get default company safely
    company = frappe.defaults.get_user_default("Company")

    # 2️⃣ If default company is not set, try fallback
    if not company:
        # Optionally, pick the first company user has permission for
        permitted_companies = frappe.get_all(
            "User Permission",
            filters={
                "user": user,
                "allow": "Company"
            },
            fields=["for_value"]
        )
        if permitted_companies:
            company = permitted_companies[0].for_value
        else:
            return {}  # no company at all

    # 3️⃣ Try to get company document safely
    try:
        company_doc = frappe.get_doc("Company", company)
    except frappe.DoesNotExistError:
        return {}  # company deleted or invalid

    # 4️⃣ Build branding object, fallback to None if fields missing
    return {
        "company": company,
        "logo": getattr(company_doc, "custom_brand_logo", None),
        "primary_color": getattr(company_doc, "custom_brand_primary_color", None),
        "secondary_color": getattr(company_doc, "custom_brand_secondary_color", None),
        "favicon": getattr(company_doc, "custom_brand_favicon", None),
        "custom_css": getattr(company_doc, "custom_brand_css", None),
    }
