document.addEventListener('DOMContentLoaded', function() {
    var jobs = JSON.parse(localStorage.getItem('jobs')) || [];
    var table = document.querySelector('.table');
    var tbody = document.getElementById('mb-4'); 
    function displayJobs() {  
        tbody.innerHTML = '';
        jobs.forEach(function(job) {
            var row = document.createElement('tr');
            row.innerHTML = `
                <td>${job.id}</td>
                <td>${job.title}</td>
                <td>${job.salary}</td>
                <td>${job.company}</td>
                <td>${job.status}</td>
                <td><button class="edit">Edit</button><button class="delete">Delete</button></td>
            `;
            tbody.appendChild(row);
        });
    }

    function removeRow(row) {
        var id = row.cells[0].textContent;
        row.remove();
        var updatedData = jobs.filter(function(item) {
            return item.id !== id;
        });
        jobs = updatedData;
        localStorage.setItem('jobs', JSON.stringify(jobs));
    }

    function editRow(row) {
        var cells = row.cells;
        for (var i = 0; i < cells.length - 1; i++) {
            var content = cells[i].textContent;
            cells[i].innerHTML = `<input type="text" value="${content}">`;
        }
        var editButton = row.querySelector('.edit');
        editButton.textContent = 'Save';
        editButton.classList.remove('edit');
        editButton.classList.add('save');
    }
    function saveRow(row) {
        var cells = row.cells;
        var rowIndex = row.rowIndex - 1;
        jobs[rowIndex] = {
            id: cells[0].querySelector('input').value,
            title: cells[1].querySelector('input').value,
            salary: cells[2].querySelector('input').value,
            company: cells[3].querySelector('input').value,
            status: cells[4].querySelector('input').value
        };
        
        displayJobs();
    }

    table.addEventListener('click', function(event) {
        var target = event.target;
        if (target.classList.contains('delete')) {
            var row = target.closest('tr');
            removeRow(row);
        } else if (target.classList.contains('edit')) {
            var row = target.closest('tr');
            editRow(row);
        } else if (target.classList.contains('save')) {
            var row = target.closest('tr');
            saveRow(row);
        }
    });

    document.getElementById('job-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var id = document.getElementById('job-id').value;
        var title = document.getElementById('job-title').value;
        var salary = document.getElementById('job-salary').value;
        var company = document.getElementById('job-company-name').value;
        var status = document.getElementById('job-status').value;
        var job = {
            id: id,
            title: title,
            salary: salary,
            company: company,
            status: status
        };
        jobs.push(job);
        localStorage.setItem('jobs', JSON.stringify(jobs));
        displayJobs();
        document.getElementById('job-form').reset();
    });

    displayJobs();
});
