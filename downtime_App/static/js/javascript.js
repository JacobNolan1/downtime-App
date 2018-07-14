$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });

    $('#activities-category').change(selectActivities);
    $('#activities-list').change(callAjax);
});

function selectActivities() {

	var category = ($('#activities-category').val());
	$('#activities-list').children().remove();
	if(category === "General") {
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
    BuyMagic : 'Buy Magical Item',
    SellMagic : 'Sell Magical Item',
    BuyNonMagic : 'Buy Non-Magical Item',
    SellNonMagic : 'Sell Non-Magical Item',
    CraftItem : 'Craft Item',
    Carouse : 'Carouse',
    Training : 'Training',
    Relax : 'Relaxation',
    Research : 'Research',
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

function callAjax() {
	$( "#included-activityDetails" ).remove();
    $.ajax({
        url: 'http://127.0.0.1:5000/character/activities/ajax',
        data: { 
        	"selected_category": $('#activities-category').val(),
        	"selected_activity": $('#activities-list').val() 
      	},
        type: 'GET',
        dataType : "html",
        success: function(response) {
            console.log(response);
            $("#activityDetails").append(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

