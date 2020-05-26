const days = document.querySelectorAll(".isClickable");
alert('Select your event');
[...days].map((day, i) => {
  console.log(day);
  day.addEventListener('click', (event) => {
    alert(`Day: ${day.innerText}`);
  });
});



