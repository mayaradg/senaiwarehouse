function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue, tbody;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("feedstock-table");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    id = tr[i].getElementsByTagName("td")[0];
    if (td && id) {
      txtValue = td.textContent || td.innerText;
      idValue = id.textContent || id.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1 || idValue.indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}