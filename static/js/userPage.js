/* document.addEventListener('DOMContentLoaded', function() {
    var jobs = JSON.parse(localStorage.getItem('jobs')) || [];
    var appliedJobs = JSON.parse(localStorage.getItem('appliedJobs')) || [];
    var tbody = document.getElementById('mb-4');
    var table_2 = document.getElementById('table-2');
    function displayJobs() {
        tbody.innerHTML = '';
        jobs.forEach(function(job,index) {
            var row = document.createElement('tr');
            row.innerHTML = `
                <th scope="row">${index+1}</th>
                <td>${job.id}</td>
                <td>${job.title}</td>
                <td>${job.salary}</td>
                <td>${job.company}</td>
                <td><button type="button" class="btn-btn-apply">Apply</button></td>
            `;
            tbody.appendChild(row);
        });
    }
    function displayAppliedJobs() {
        table_2.innerHTML = '';
        appliedJobs.forEach(function(job,index) {
            var row = document.createElement('tr');
            row.innerHTML = `
                <th scope="row">${index+1}</th>
                <td>${job.id}</td>
                <td>${job.title}</td>
            `;
            table_2.appendChild(row);
        });
    }
    function addToAppliedJobs(job) {
        appliedJobs.push(job);
        localStorage.setItem('appliedJobs', JSON.stringify(appliedJobs));
        displayAppliedJobs();
    }
    tbody.addEventListener('click', function(event) {
        if (event.target.classList.contains('btn-btn-apply')) {
            var row = event.target.closest('tr');
            var job = {
                id: row.cells[1].textContent,
                title: row.cells[2].textContent,
                salary: row.cells[3].textContent,
                company: row.cells[4].textContent
            };
            addToAppliedJobs(job);
            window.location.href='Apply.html';
        }
    });
    displayJobs();
    displayAppliedJobs();
}); */

function myFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("exampleFormControlInput1")
    filter = input.value.toUpperCase();
    table = document.getElementById("tb");
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1)
            {
                tr[i].style.display = "";
            }
            else {
                tr[i].style.display = "none";
            }
        }       
    }
}