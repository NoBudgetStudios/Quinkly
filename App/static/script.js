document.getElementById("gen-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const form = e.target;
  const data = {
    topic: form.topic.value,
    tone: form.tone.value,
    style: form.style.value,
    keywords: form.keywords.value.split(",").map(k => k.trim()),
    output_type: form.output_type.value
  };

  const res = await fetch("/generate_content", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const json = await res.json();
  document.getElementById("output").textContent = json.output || "No output.";
});
