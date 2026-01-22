import frappe

def setup_custom_fields():
    """
    Create Branding tab and fields in Company doctype
    Safe to run multiple times
    """

    custom_fields = {
        "Company": [
            # --- Branding Tab ---
            {
                "fieldname": "custom_branding_tab",
                "label": "Branding",
                "fieldtype": "Tab Break",
                "insert_after": "dashboard_tab",
            },

            # --- Logo ---
            {
                "fieldname": "custom_brand_logo",
                "label": "Brand Logo",
                "fieldtype": "Attach Image",
                "insert_after": "custom_branding_tab",
            },

            # --- Favicon ---
            {
                "fieldname": "custom_brand_favicon",
                "label": "Brand Favicon",
                "fieldtype": "Attach Image",
                "insert_after": "custom_brand_logo",
                "description": "Recommended: 32x32 PNG",
            },

            # --- Primary Color ---
            {
                "fieldname": "custom_brand_primary_color",
                "label": "Brand Primary Color",
                "fieldtype": "Color",
                "insert_after": "custom_brand_logo",
            },

            # --- Secondary Color ---
            {
                "fieldname": "custom_brand_secondary_color",
                "label": "Brand Secondary Color",
                "fieldtype": "Color",
                "insert_after": "custom_brand_primary_color",
            },

            # --- Custom CSS ---
            {
                "fieldname": "custom_brand_css",
                "label": "Brand CSS",
                "fieldtype": "Code",
                "options": "CSS",
                "insert_after": "custom_brand_secondary_color",
            },
        ]
    }

    create_custom_fields(custom_fields)


def create_custom_fields(custom_fields):
    """
    Create custom fields if they do not already exist
    """
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

    create_custom_fields(custom_fields, ignore_validate=True)
