function goBack() {
  window.history.back();
}

if (window.location.pathname === "/signIn") {
  document
    .getElementById("signInForm")
    .addEventListener("submit", async function (event) {
      event.preventDefault();

      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      const encoder = new TextEncoder();
      const data = encoder.encode(password);
      const hashBuffer = await crypto.subtle.digest("SHA-256", data);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hashedPassword = hashArray
        .map((b) => b.toString(16).padStart(2, "0"))
        .join("");

      const response = await fetch("/authRecieve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          sentFrom: "/signIn",
          email: email,
          password: hashedPassword,
        }),
      });

      const result = await response.json();
      alert(result.message);
    });
}

if (window.location.pathname === "/signUp") {
}
