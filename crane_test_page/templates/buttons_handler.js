var SCRIPT_ROOT= "http://192.168.88.33:5000";
$(function() {
    $('#left_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/left_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#up_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/up_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#down_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/down_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#right_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/right_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#up_cargo_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/up_cargo_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#down_cargo_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/down_cargo_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#solenoid_on_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/solenoid_on_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#solenoid_off_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/solenoid_off_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#auto_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/auto_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#return_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/return_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});
$(function() {
    $('#exit_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/exit_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});