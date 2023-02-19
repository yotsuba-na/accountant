function setFormData(data, formDataId = "mainFormData") {
  const mainFormData = document.getElementById(formDataId);
  mainFormData.value = JSON.stringify(data);
}

function setDateFilter() {
  const selectors = ["selectDate", "selectDateQuery"];
  const data = {};
  for (var i = 0; i < selectors.length; i++) {
    let selectorId = selectors[i];
    const selector = document.getElementById(selectorId);
    data[selectorId] = selector.options[selector.selectedIndex].value;
  }
  setFormData(data);
}

