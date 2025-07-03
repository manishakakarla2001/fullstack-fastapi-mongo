const API_URL = "http://localhost:8000/items/";

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("itemForm");
  const itemList = document.getElementById("itemList");

  // Load existing items
  fetch(API_URL)
    .then(res => res.json())
    .then(items => {
      items.forEach(addItemToDOM);
    });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const description = document.getElementById("description").value.trim();

    if (!name || !description) return;

    const newItem = { name, description };

    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newItem),
    });

    const savedItem = await response.json();
    addItemToDOM(savedItem);
    form.reset();
  });

  function addItemToDOM(item) {
    const li = document.createElement("li");
    li.textContent = `${item.name}: ${item.description}`;
    itemList.appendChild(li);
  }
});
