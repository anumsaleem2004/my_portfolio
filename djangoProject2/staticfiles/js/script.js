/*
document.addEventListener('DOMContentLoaded', function() {
    function setupAddFunctionality(buttonId, inputContainerId, inputId, listId, url) {
        document.getElementById(buttonId).addEventListener('click', function() {
            document.getElementById(inputContainerId).style.display = 'block';
        });

        document.getElementById(`submit${inputId.charAt(0).toUpperCase() + inputId.slice(1)}Button`).addEventListener('click', function() {
            const newValue = document.getElementById(inputId).value;
            if (newValue.trim() === '') {
                alert('Input cannot be empty.');
                return;
            }

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({ content: newValue })
            }).then(response => response.json())
              .then(data => {
                  if (data.success) {
                      const listItem = document.createElement('li');
                      listItem.textContent = newValue;
                      document.getElementById(listId).appendChild(listItem);
                      document.getElementById(inputContainerId).style.display = 'none';
                      document.getElementById(inputId).value = '';
                  } else {
                      alert('Failed to add item: ' + data.error);
                  }
              }).catch(error => {
                  console.error('Error:', error);
                  alert('An error occurred. Please try again.');
              });
        });
    }

    function loadItems(url, containerId) {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById(containerId);
                container.innerHTML = ''; // Clear existing items
                data.items.forEach(item => {
                    const listItem = document.createElement('li');
                    listItem.textContent = item.name || item.title + ': ' + (item.description || item.company + ' (' + item.start_date + ' - ' + (item.end_date || 'Present') + '): ' + item.description);
                    container.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    setupAddFunctionality('addSkillButton', 'skillInputContainer', 'newSkillInput', 'skillsContainer', '{% url "add_skill" %}');
    setupAddFunctionality('addProjectButton', 'projectInputContainer', 'newProjectInput', 'projectsList', '{% url "add_project" %}');
    setupAddFunctionality('addExperienceButton', 'experienceInputContainer', 'newExperienceInput', 'experienceList', '{% url "add_experience" %}');
    setupAddFunctionality('addEducationButton', 'educationInputContainer', 'newEducationInput', 'educationList', '{% url "add_education" %}');
    setupAddFunctionality('addCertificationButton', 'certificationInputContainer', 'newCertificationInput', 'certificationsList', '{% url "add_certification" %}');

    // Load items initially
    loadItems('{% url "get_skills" %}', 'skillsContainer');
    loadItems('{% url "get_projects" %}', 'projectsList');
    loadItems('{% url "get_experiences" %}', 'experienceList');
    loadItems('{% url "get_education" %}', 'educationList');
    loadItems('{% url "get_certifications" %}', 'certificationsList');
});
*/
