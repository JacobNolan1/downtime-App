$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });

    $('#activities-category').change(selectActivities);
});

function selectActivities() {

	var category = ($('#activities-category').val());
	$('#activities-list').children().remove();
	if(category === "General Activities") {
		selectGeneral();
	} else if(category === "Job") {
		selectJob();
	} else if(category === "Town") {
		selectTown();
	} else if(category === "City") {
		selectCity();
	} else if(category === "Wilderness") {
		selectWilderness();
	} else if(category === "Dungeon") {
		selectDungeon();
	} else if(category === "Other") {
		selectOther();
	} else {
		alert("Not Selected");
	}
}

function selectGeneral() {
	var activities = {
    val1 : '--Select--',
    val2 : 'Craft an Item',
    val3 : 'Buy an Item',
    val4 : 'Sell an Item'
	};
	setSelectElements(activities);
}

function selectJob() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function selectTown() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function selectCity() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function selectWilderness() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function selectDungeon() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function selectOther() {
	var activities = {
    val1 : '--Select--',
    val2 : '---',
    val3 : '---',
    val4 : '---'
	};
	setSelectElements(activities);
}

function setSelectElements(activities) {
	$.each(activities, function(key, value) {
     $('#activities-list')
         .append($("<option></option>")
         .attr("value",key)
         .text(value));
     });
}
