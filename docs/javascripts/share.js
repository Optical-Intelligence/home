document.addEventListener("click", async (event) => {
  const button = event.target.closest(".share-buttons__copy");

  if (!button) return;

  try {
    await navigator.clipboard.writeText(button.dataset.shareUrl);
    button.textContent = "Copied!";
    window.setTimeout(() => {
      button.textContent = "Copy link";
    }, 2000);
  } catch {
    button.textContent = "Copy unavailable";
  }
});
