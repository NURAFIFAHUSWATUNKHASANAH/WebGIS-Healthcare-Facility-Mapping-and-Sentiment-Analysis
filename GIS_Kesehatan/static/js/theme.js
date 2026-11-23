document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.getElementById("toggleTheme");
    const themeText = document.getElementById("themeText");

    // Ambil tema dari localStorage
    const currentTheme =
        localStorage.getItem("theme") || "dark";

    // Set tema saat halaman dibuka
    document.documentElement.setAttribute(
        "data-theme",
        currentTheme
    );

    // Sinkronkan posisi switch
    if (toggle) {

        toggle.checked = currentTheme === "light";

        if (themeText) {
            themeText.textContent =
                currentTheme === "light"
                    ? "Light Mode"
                    : "Dark Mode";
        }

        toggle.addEventListener("change", () => {

            const newTheme =
                toggle.checked
                    ? "light"
                    : "dark";

            document.documentElement.setAttribute(
                "data-theme",
                newTheme
            );

            localStorage.setItem(
                "theme",
                newTheme
            );

            if (themeText) {
                themeText.textContent =
                    newTheme === "light"
                        ? "Light Mode"
                        : "Dark Mode";
            }

        });

    }

});