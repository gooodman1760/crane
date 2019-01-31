var SCRIPT_ROOT= "http://192.168.43.104:5000";

$(function() {
    $('#left_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/left_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#up_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/up_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#down_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/down_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#right_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/right_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#up_cargo_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/up_cargo_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#down_cargo_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/down_cargo_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#solenoid_on_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/solenoid_on_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#solenoid_off_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/solenoid_off_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#auto_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/auto_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#return_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/return_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });

    $('#exit_button').bind('click', function() {
    $.getJSON(SCRIPT_ROOT + '/exit_button', {
    }, function(data) {
        $("#result").text(data.result);
    });
    return false;
    });
});