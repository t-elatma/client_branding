import frappe

def cleanup():
    """
    Remove custom branding fields from Company
    Safe to run multiple times
    """

    branding_fields = [
        "custom_branding_tab",
        "custom_brand_logo",
        "custom_brand_favicon",
        "custom_brand_primary_color",
        "custom_brand_secondary_color",
        "custom_brand_css",
    ]

    delete_custom_fields("Company", branding_fields)


def delete_custom_fields(doctype, fieldnames):
    """
    Delete Custom Field records cleanly
    """
    for fieldname in fieldnames:
        try:
            frappe.delete_doc(
                "Custom Field",
                f"{doctype}-{fieldname}",
                force=True
            )
        except frappe.DoesNotExistError:
            pass

    frappe.clear_cache(doctype=doctype)
