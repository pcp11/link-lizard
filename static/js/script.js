function showConstructionWarning() {
    alert("This section is under construction.");
}

function copyToClipboard(generatedUrl) {
    const el = document.createElement("textarea");

    el.value = generatedUrl;
    document.body.appendChild(el);
    el.select();

    document.execCommand("copy");
    document.body.removeChild(el);
}

function showError(error, originalUrlInput, generatedHashInput) {
    if (error.original_url) {
        const originalUrlFeedback = document.getElementById("original-url-invalid-feedback");
        originalUrlFeedback.innerText = error.original_url.join(", ");
        originalUrlInput.classList.add("is-invalid");
    }
    if (error.generated_hash) {
        const generatedHashFeedback = document.getElementById("generated-hash-invalid-feedback");
        generatedHashFeedback.innerText = error.generated_hash.join(", ");
        generatedHashInput.classList.add("is-invalid");
    }
}

function handleGeneratedUrl(data) {
    const originalUrl = data.original_url;
    const generatedUrl = data.generated_url;
    const wrapper = document.createElement("div");

    wrapper.innerHTML = `<div class="card mb-1">
        <div class="card-body">
            <div class="row align-items-center">
                <div class="col text-truncate">
                    ${originalUrl}
                </div>
                <div class="col" style="text-align: right">
                    <div class="d-flex align-items-center justify-content-end">
                        <div class="mr-3">
                            <a id="generatedLink" href="${generatedUrl}" target="_blank">${generatedUrl}</a>
                        </div>
                        <div>
                            <button onclick="copyToClipboard(\'${generatedUrl}\')" class="btn btn-outline-secondary" type="submit">
                                Copy
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`;

    document.getElementById("generated_urls").prepend(wrapper);
    document.getElementById("form").reset();
}

document.getElementById("form").addEventListener("submit", evt => {
    const formElement = evt.srcElement;
    const originalUrlInput = document.getElementById("original_url");
    const generatedHashInput = document.getElementById("generated_hash");

    // Reset invalid state
    originalUrlInput.classList.remove("is-invalid");
    generatedHashInput.classList.remove("is-invalid");

    fetch("", {method: "POST", body: new FormData(formElement)})
        .then(response => response.json())
        .then(result => result.errors ? Promise.reject(result.errors) : Promise.resolve(result))
        .then(data => handleGeneratedUrl(data))
        .catch(error => showError(error, originalUrlInput, generatedHashInput));

    evt.preventDefault();
});