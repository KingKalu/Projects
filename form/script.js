const form = document.querySelector("#userForm");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  console.log([...formData])

  const data = Object.fromEntries(formData);

  console.log(data);
});