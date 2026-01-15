frappe.ready(() => {
    frappe.call({
        method: "client_branding.api.get_branding",
        callback: (r) => {
            if (!r.message) return;

            const b = r.message;
            console.log(b);

            applyLogo(b.logo);
            applyColors(b.primary_color, b.secondary_color);
            applyFavicon(b.favicon);
            applyCustomCSS(b.custom_css);
        }
    });
});

/* -------------------------------
   Branding helpers
-------------------------------- */

function applyLogo(logo) {
    if (!logo) return;

    const logoImg = document.querySelector(".navbar-home img");
    if (logoImg) {
        logoImg.src = logo;
    }
}

function applyColors(primary, secondary) {
    if (primary) {
        document.documentElement.style.setProperty(
            "--brand-primary",
            primary
        );
    }

    if (secondary) {
        document.documentElement.style.setProperty(
            "--brand-secondary",
            secondary
        );
    }
}

function applyFavicon(favicon) {
    if (!favicon) return;

    let link = document.querySelector("link[rel~='icon']");
    if (!link) {
        link = document.createElement("link");
        link.rel = "icon";
        document.head.appendChild(link);
    }

    link.href = favicon;
}

function applyCustomCSS(css) {
    if (!css) return;

    const style = document.createElement("style");
    style.setAttribute("data-client-branding", "true");
    style.innerHTML = css;
    document.head.appendChild(style);
}
