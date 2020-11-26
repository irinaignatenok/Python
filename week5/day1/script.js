  let nounInput = document.getElementById('noun');
  let adjectiveInput = document.getElementById('adjective');
  let nameInput = document.getElementById('person');
  let libButton = document.getElementById('lib-button');

     let libIt = function() {
        let storyDiv = document.getElementById("story");
        storyDiv.innerHTML =`One ${adjectiveInput.value} ${nounInput.value} was mady by ${nameInput.value}`
        nounInput.value = '';
        adjectiveInput.value = '';
        nameInput.value = '';
        };
    libButton.addEventListener('click', libIt);