function upload_roller(){
    $.getJSON($SCRIPT_ROOT + '/rollers/_add_roller', {
	rol_id: $('div[name="rol_id"]')[0].innerText,
	type: $('div[name="type"]')[0].innerText,
	mnfr: $('div[name="mnfr"]')[0].innerText,
	part_number: $('div[name="p_n"]')[0].innerText,
	bearing: $('div[name="bear"]')[0].innerText,
	sealing: $('div[name="cont"]')[0].innerText
    }, function(data) {
	// console.log(data)
	if (data.Status === 'SUCCESS') {
	    window.location.reload();
	}
    });
}

function new_event(){
    $.getJSON($SCRIPT_ROOT + '/history/_add_event', {
	date_string: $('input[name="date_string"]')[0].value,
	rol_id: $('select[name="r_id"]')[0].value,
	rig_name: $('select[name="rig_name"]')[0].value,
	st_id: $('div[name="st_id"]')[0].innerText,
	action: $('div[name="action"]')[0].innerText
    }, function(data) {
	// console.log(data)
	if (data.Status === 'SUCCESS') {
	    window.location.reload();
	}
    });
}

function update_history(_var){
    console.log(_var)
    $.getJSON($SCRIPT_ROOT + '/history', {
	rig_id: _var.value,
    }, function() {
	window.location.reload();
    });
}
