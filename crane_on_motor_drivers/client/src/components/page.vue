<template>
  <div class="page">
          <p class="project_title">Raspberry Pi - Crane Camera</p>
      <center><img src="stream.mjpg" width="640" height="480"></center>
      <div class="buttons">
          <div>
              <div>
                  <button type="button" @click="left_method">Left</button>
              <div>
                  <button type="button" @click="up_method">Up</button>
                  <button type="button" @click="down_method">Down</button>
              </div>
                  <button type="button" @click="right_method">Right</button>
              </div>
          </div>
      </div>
      <div class="buttons">
          <div>
              <button type="button" @click="up_c_method">Up Cargo</button>
              <button type="button" @click="down_c_method">Down Cargo</button>
          </div>
          <div>
              <button type="button" @click="solenoid_on_method">Solenoid ON</button>
              <button type="button" @click="solenoid_off_method">Solenoid OFF</button>
          </div>
          <div>
              <button type="button" @click="auto_method">AUTO</button>
              <button type="button" @click="return_method">RETURN</button>
          </div>
      </div>
      <center><button class="exit_button" @click="quit_method">Exit</button></center>
      <p>Some messages: {{ is_something }}</p>
  </div>
</template>

<script>
import ControlLR from '../../../controllers/control_lr.py'
import ControlUD from '../../../controllers/control_ud.py'
import ControlUDC from '../../../controllers/control_ud_c.py'
import ControlSolenoid from '../../../controllers/control_solenoid.py'
import ControlAuto from '../../../controllers/auto_control.py'
export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    left_method () {
      ControlLR.do_left()
    },
    up_method () {
      ControlUD.do_up()
    },
    down_method () {
      ControlUD.do_down()
    },
    right_method () {
      ControlLR.do_right()
    },
    up_c_method () {
      ControlUDC.do_up_cargo()
    },
    down_c_method () {
      ControlUDC.do_down_cargo()
    },
    solenoid_on_method () {
      ControlSolenoid.solenoid_on()
    },
    solenoid_off_method () {
      ControlSolenoid.solenoid_off()
    },
    auto_method () {
      ControlAuto.auto_control()
    },
    return_method () {

    },
    quit_method () {

    }
  },
  created () {
    this.left_method()
    this.right_method()
    this.up_method()
    this.down_method()
    this.up_c_method()
    this.down_c_method()
    this.solenoid_on_method()
    this.solenoid_off_method()
  }
}
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .page{
        background: linear-gradient(to right, #FFFFFF, #6DD5FA, #2980B1);
    }
    .project_title{
        text-align: center;
        font: 30px Estrangelo Edessa, sans-serif;
        font-weight: bold;
        margin: 15px;
    }
    .buttons{
        display: flex;
    flex-direction: row;
        margin-top: 20px;
        justify-content: center;
    }
    .buttons > div{
        display: flex;
    flex-direction: column;
    }
    .buttons > div > div{
        display: flex;
    flex-direction: row;
        margin-right: 30px;
        background-color: #16CEFF;
    }
    .buttons > div > div > div{
        display: flex;
    flex-direction: column;
    }
    button{
        font: 25px Estrangelo Edessa, sans-serif;
        background-color: aliceblue;
        margin: 5px;
        padding: 10px;
        border-radius: 5px;
    }
    button:hover, button:active{
        background-color: #C3F1F9;
    }
    img{
        border-style: solid;
    }
    .exit_button{
        font: 30px Estrangelo Edessa, sans-serif;
        background-color: #FF593B;
        margin: 10px;
        padding: 10px;
        width: 400px;
        border-radius: 5px;
    }
    .exit_button:hover, .exit_button:active{
        background-color: #FF883B;
    }
</style>
