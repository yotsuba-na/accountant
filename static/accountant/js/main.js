/* Filters
 */

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


/* Transactions
 */

function showTransactionTypeFields(selector) {
  // TODO: Rename variables
  const selectedValue = selector.options[selector.selectedIndex].value;
  const transactionTypeFields = ["transactionTransferFields"];

  for (var i = 0; i < transactionTypeFields.length; i++) {
    const transactionTypeId = transactionTypeFields[i];
    transactionTypeField = document.getElementById(transactionTypeId);

    if (transactionTypeId.includes(selectedValue)) {
      transactionTypeField.style.display = "block";
    } else {
      transactionTypeField.style.display = "none";
    }

  }
}
