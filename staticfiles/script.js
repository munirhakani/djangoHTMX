;(function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))

    htmx.on("create_pk", (e) => {
        htmx.ajax('GET', 'object/'+e.detail.value+'/', {
            target:'#target', swap:'outerHTML', values: {'create': true, },
        })
        modal.hide()
	})

    htmx.on("update_pk", (e) => {
        htmx.ajax('GET', 'object/'+e.detail.value+'/', {
            target:'#object-' + e.detail.value, swap:'outerHTML',
        })
        modal.hide()
	})

    htmx.on("shown.bs.modal", () => {
        $('#formModal').find('input[type=text],textarea,select').filter(':visible:first').focus();
        // $('#formModal').find('input[type=text],textarea,select').filter(':visible:first').select();
    })

    htmx.on("hidden.bs.modal", () => {
        document.getElementById("dialog").innerHTML = ""
    })
})()