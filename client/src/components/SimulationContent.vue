<template>
    <div class="simulasi-container grid col-auto p-0 m-0">
        <div class="simulasi-container-horizontal grid text-white text-left font-bold m-1 p-0 align-middle text-xs lg:text-xl">
            <p>Komponen</p>
            <p>Nama Komponen</p>
            <p>Harga</p>
        </div>
        <!-- gw tambahin yg di bawah comment ini -->
        <form v-on:submit.prevent="loadsaveBuild">
        <!-- gw tambahin yg di atas comment ini -->    
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>CPU</p>
            <div class="komp-selection">
                <label for="cpu"></label>
                    <select v-model="build.cpu" name="cpu" id="cpu" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose CPU</option>
                        <option v-for="cpu in cpus" :value="cpu.Name" :key="cpu.id">{{ cpu.Name }}</option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>

        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Motherboard</p>
            <div class="komp-selection">
                <label for="motherboard"></label>
                    <select v-model="build.motherboard" id="motherboard" name="motherboard" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Motherboard</option>
                        <option v-for="motherboard in motherboards" :value="motherboard.brand + ' ' + motherboard.model + ' ' + motherboard.socket + ' ' + motherboard.form_factor" :key="motherboard.id">
                            {{ motherboard.brand }} {{motherboard.model}} {{motherboard.socket}} {{motherboard.form_factor}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Memory</p>
            <div class="komp-selection">
                <label for="memory"></label>
                    <select v-model="build.memory" id="memory" name="memory" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Memory</option>
                        <option v-for="memory in memorys" :value="memory.brand + ' ' + memory.model + ' ' + memory.module_type + ' ' + memory.speed_cycles" :key="memory.id">
                            {{ memory.brand }} {{memory.model}} {{memory.module_type}} {{memory.speed_cycles}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>  
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Graphics Card</p>
            <div class="komp-selection">
                <label for="graphicsCard"></label>
                    <select v-model="build.video_card" id="graphicsCard" name="graphicsCard" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Graphics Card</option>
                        <option v-for="video_card in video_cards" :value="video_card.brand + ' ' + video_card.brand + ' ' + video_card.chipset + ' ' + video_card.vram_total" :key="video_card.id">
                            {{ video_card.brand }} {{video_card.chipset}} {{video_card.vram_total}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Power Supply</p>
            <div class="komp-selection">
                <label for="powerSupply"></label>
                    <select v-model="build.power_supply" id="powerSupply" name="powerSupply" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Power Supply</option>
                        <option v-for="power_supply in power_supplys" :value="power_supply.brand + ' ' + power_supply.model + ' ' + power_supply.efficiency_rating + ' ' + power_supply.wattage" :key="power_supply.id">
                            {{ power_supply.brand }} {{power_supply.model}} {{power_supply.efficiency_rating}} {{power_supply.wattage}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Case</p>
            <div class="komp-selection">
                <label for="case"></label>
                    <select v-model="build.case" id="case" name="case" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Case</option>
                        <option v-for="i in cases" :value="i.brand + ' ' + i.model + ' ' + i.form_factor + ' ' + i.color" :key="i.id">
                            {{ i.brand }} {{i.model}} {{i.form_factor}} {{i.color}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div> 
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Hard Drive 1</p>
            <div class="komp-selection">
                <label for="hardDrive"></label>
                    <select v-model="build.internal_hard_drive" id="hardDrive" name="hardDrive" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Hard Drive</option>
                        <option v-for="internal_hard_drive in internal_hard_drives" :value="internal_hard_drive.brand + ' ' + internal_hard_drive.model + ' ' + internal_hard_drive.capacity_total + ' ' + internal_hard_drive.storage_type + ' ' + internal_hard_drive.interface" :key="internal_hard_drive.id">
                            {{ internal_hard_drive.brand }} {{internal_hard_drive.model}} {{internal_hard_drive.capacity_total}} {{internal_hard_drive.storage_type}} {{internal_hard_drive.interface}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div> 
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Keyboard</p>
            <div class="komp-selection">
                <label for="keyboard"></label>
                    <select v-model="build.keyboard" id="keyboard" name="keyboard" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Keyboard</option>
                        <option v-for="keyboard in keyboards" :value="keyboard.brand + ' ' + keyboard.style + ' ' + keyboard.switches + ' ' + keyboard.backlight + ' ' + keyboard.connection" :key="keyboard.id">
                            {{ keyboard.brand }} {{keyboard.model}} {{keyboard.style}} {{keyboard.switches}} {{keyboard.backlight}} {{keyboard.connection}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Mouse</p>
            <div class="komp-selection">
                <label for="mouse"></label>
                    <select v-model="build.mouse" id="mouse" name="mouse" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Mouse</option>
                        <option v-for="mouse in mouses" :value="mouse.brand + ' ' + mouse.model + ' ' + mouse.connection" :key="mouse.id">
                            {{ mouse.brand }} {{mouse.model}} {{mouse.connection}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Monitor</p>
            <div class="komp-selection">
                <label for="monitor"></label>
                    <select v-model="build.monitor" id="monitor" name="monitor" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Monitor</option>
                        <option v-for="monitor in monitors" :value="monitor.brand + ' ' + monitor.model + ' ' + monitor.size + ' ' + monitor.panel_type" :key="monitor.id">
                            {{ monitor.brand }} {{monitor.model}} {{monitor.size}} {{monitor.panel_type}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>CPU Cooler</p>
            <div class="komp-selection">
                <label for="cpu_cooler"></label>
                    <select v-model="build.cpu_cooler" id="cpu_cooler" name="cpu_cooler" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose CPU Cooler</option>
                        <option v-for="cpu_cooler in cpu_coolers" :value="cpu_cooler.brand + ' ' + cpu_cooler.model + ' ' + cpu_cooler.color" :key="cpu_cooler.id">
                            {{ cpu_cooler.brand }} {{cpu_cooler.model}} {{cpu_cooler.color}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Case Fan</p>
            <div class="komp-selection">
                <label for="caseFan"></label>
                    <select v-model="build.case_fan" id="caseFan" name="caseFan" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Case Fan</option>
                        <option v-for="case_fan in case_fans" :value="case_fan.brand + ' ' + case_fan.model + ' ' + case_fan.size + ' ' + case_fan.color" :key="case_fan.id">
                            {{ case_fan.brand }} {{case_fan.model}} {{case_fan.size}} {{case_fan.color}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Wireless Network Card</p>
            <div class="komp-selection">
                <label for="wireless_network_card"></label>
                    <select v-model="build.wireless_network_card" id="wireless_network_card" name="wireless_network_card" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Wireless Network Card</option>
                        <option v-for="wireless_network_card in wireless_network_cards" :value="wireless_network_card.brand + ' ' + wireless_network_card.model + ' ' + wireless_network_card.supported_protocols + ' ' + wireless_network_card.interface" :key="wireless_network_card.id">
                            {{ wireless_network_card.brand }} {{wireless_network_card.model}} {{wireless_network_card.supported_protocols}} {{wireless_network_card.interface}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Wired Network Card</p>
            <div class="komp-selection">
                <label for="wired_network_card"></label>
                    <select v-model="build.wired_network_card" id="wired_network_card" name="wired_network_card" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Wired Network Card</option>
                        <option v-for="wired_network_card in wired_network_cards" :value="wired_network_card.brand + ' ' + wired_network_card.model + ' ' + wired_network_card.interface" :key="wired_network_card.id">
                            {{ wired_network_card.brand }} {{wired_network_card.model}} {{wired_network_card.interface}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Optical Drive</p>
            <div class="komp-selection">
                <label for="optical_drive"></label>
                    <select v-model="build.optical_drive" id="optical_drive" name="optical_drive" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Optical Drive</option>
                        <option v-for="optical_drive in optical_drives" :value="optical_drive.brand + ' ' + optical_drive.model" :key="optical_drive.id">
                            {{ optical_drive.brand }} {{optical_drive.model}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Sound Card</p>
            <div class="komp-selection">
                <label for="sound_card"></label>
                    <select v-model="build.sound_card" id="sound_card" name="sound_card" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Sound Card</option>
                        <option v-for="sound_card in sound_cards" :value="sound_card.brand + ' ' + sound_card.model + ' ' + sound_card.interface" :key="sound_card.id">
                            {{ sound_card.brand }} {{sound_card.model}} {{sound_card.interface}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Speakers</p>
            <div class="komp-selection">
                <label for="speakers"></label>
                    <select v-model="build.speakers" id="speakers" name="speakers" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Speakers</option>
                        <option v-for="speakers in speakerss" :value="speakers.brand + ' ' + speakers.model" :key="speakers.id">
                            {{ speakers.brand }} {{speakers.model}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Headphones</p>
            <div class="komp-selection">
                <label for="headphones"></label>
                    <select v-model="build.headphones" id="headphones" name="headphones" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Headphones</option>
                        <option v-for="headphones in headphoness" :value="headphones.brand + ' ' + headphones.model + ' ' + headphones.form_factor" :key="headphones.id">
                            {{ headphones.brand }} {{headphones.model}} {{headphones.form_factor}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>UPS</p>
            <div class="komp-selection">
                <label for="ups"></label>
                    <select v-model="build.ups" id="ups" name="ups" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose UPS</option>
                        <option v-for="ups in upss" :value="ups.brand + ' ' + ups.model + ' ' + ups.watt_capacity + ' ' + ups.va_capacity" :key="ups.id">
                            {{ ups.brand }} {{ups.model}} {{ups.watt_capacity}} {{ups.va_capacity}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <div class="simulasi-container-horizontal text-xs lg:text-xl">
            <p>Thermal Paste</p>
            <div class="komp-selection">
                <label for="thermal_paste"></label>
                    <select v-model="build.thermal_paste" id="thermal_paste" name="thermal_paste" class="form-control" tabindex="12">
                        <option value="" selected disabled hidden>Choose Thermal Paste</option>
                        <option v-for="thermal_paste in thermal_pastes" :value="thermal_paste.brand + ' ' + thermal_paste.model + ' ' + thermal_paste.amount" :key="thermal_paste.id">
                            {{ thermal_paste.brand }} {{thermal_paste.model}} {{thermal_paste.amount}}
                        </option>
                    </select>
            </div>
            <p>Rp.x.xxx.xxx</p>
            
        </div>
        <!-- gw tambahin yg di bawah comment ini -->
        <input v-model="build.title" type="text" placeholder="Type Your Build's Name Here..." class="text-white outline-none inline-block text-base md:text-xl align-middle relative w-full mt-10 px-5 py-4 bg-loginB border-solid border-green1 border-2 rounded-3xl">
        <button type="submit" class="save-btn border-none text-black w-full my-10 px-2 py-4 font-bold text-base md:text-xl text-center inline-block rounded-3xl bg-green1 cursor-pointer">Save</button>
        </form>
        <!-- gw tambahin yg di atas comment ini -->
    </div>
        
        <!-- <button  @click="() => ToggleSave('buttonTrigger')" class="saveBuild-btn text-black w-full h-12 bg-green1 my-5 text-center inline-block text-xl cursor-pointer ">Save Build</button> 
        <SavePop v-if="saveTriggers.buttonTrigger" :ToggleSave="() => ToggleSave('buttonTrigger')" ></SavePop> -->
</template>

<script>
// import { ref } from 'vue'
import axios from 'axios'
import { ref } from 'vue'

export default {
  data() {
    return {
        cpus: [],
        motherboards: [],
        memorys: [],
        internal_hard_drives: [],
        cases: [],
        video_cards: [],
        power_supplys: [],
        keyboards: [],
        mouses: [],
        monitors: [],
        cpu_coolers: [],
        case_fans: [],
        wireless_network_cards: [],
        wired_network_cards: [],
        optical_drives: [],
        sound_cards: [],
        speakerss: [],
        headphoness: [],
        upss: [],
        thermal_pastes: [],
        errors: [],
        saveBuild: [],
        build: {
            title: '',
            cpu: '',
            motherboard: '',
            memory: '',
            internal_hard_drive: '',
            case: '',
            video_card: '',
            power_supply: '',
            keyboard: '',
            mouse: '',
            monitor: '',
            cpu_cooler: '',
            case_fan: '',
            wireless_network_card: '',
            wired_network_card: '',
            optical_drive: '',
            sound_card: '',
            speakers: '',
            headphones: '',
            ups: '',
            thermal_paste: ''
        }
    }
  },
  // Fetches posts when the component is created.
  async mounted() {
    this.loadcpu();
    this.loadmotherboard();
    this.loadmemory();
    this.loadinternal_hard_drive();
    this.loadcase();
    this.loadvideo_card();
    this.loadpower_supply();
    this.loadkeyboard();
    this.loadmouse();
    this.loadmonitor();
    this.loadcpu_cooler();
    this.loadcase_fan();
    this.loadwireless_network_card();
    this.loadwired_network_card();
    this.loadoptical_drive();
    this.loadsound_card();
    this.loadspeakers();
    this.loadheadphones();
    this.loadups();
    this.loadthermal_paste();
  },
  methods: {
    async loadcpu(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/cpu`)
    this.cpus = response.data
    },
    async loadmotherboard(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/motherboard`)
    this.motherboards = response.data
    },
    async loadmemory(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/memory`)
    this.memorys = response.data
    },
    async loadinternal_hard_drive(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/internal_hard_drive`)
    this.internal_hard_drives = response.data
    },
    async loadcase(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/case`)
    this.cases = response.data
    },
    async loadvideo_card(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/video_card`)
    this.video_cards = response.data
    },
    async loadpower_supply(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/power_supply`)
    this.power_supplys = response.data
    },
    async loadkeyboard(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/keyboard`)
    this.keyboards = response.data
    },
    async loadmouse(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/mouse`)
    this.mouses = response.data
    },
    async loadmonitor(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/monitor`)
    this.monitors = response.data
    },
    async loadcpu_cooler(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/cpu_cooler`)
    this.cpu_coolers = response.data
    },
    async loadcase_fan(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/case_fan`)
    this.case_fans = response.data
    },
    async loadwireless_network_card(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/wireless_network_card`)
    this.wireless_network_cards = response.data
    },
    async loadwired_network_card(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/wired_network_card`)
    this.wired_network_cards = response.data
    },
    async loadoptical_drive(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/optical_drive`)
    this.optical_drives = response.data
    },
    async loadsound_card(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/sound_card`)
    this.sound_cards = response.data
    },
    async loadspeakers(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/speakers`)
    this.speakerss = response.data
    },
    async loadheadphones(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/headphones`)
    this.headphoness = response.data
    },
    async loadups(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/ups`)
    this.upss = response.data
    },
    async loadthermal_paste(){
    const response = await axios.get(`https://34.101.183.41:5000/api/v1/parts/thermal_paste`)
    this.thermal_pastes = response.data
    },
    async loadsaveBuild(){
      const response = await axios.post(`https://34.101.183.41:5000/api/v1/builds/`, this.build)
      this.saveBuild = response.data
    }
  }
}
</script>

<script setup>
// import SavePop from './SavePop.vue'
// const saveTriggers = ref({
//     buttonTrigger:false
// });
// const ToggleSave = (trigger) => {
//     saveTriggers.value[trigger] = !saveTriggers.value[trigger]
// }
</script>

<style scoped>
.simulasi-container-horizontal{
    grid-template-columns: 20% 60% 20%;
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
}
.simluasi-boldtext{
    font-weight: 700;
}
.komp-selection option, .komp-selection select{
    background-color: black;
    color: white;
    border: none;
    width: 95%;
    height: 100%;
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    /* font-size: 18px; */
}
.simulasi-container-horizontal{
    display: grid;
    grid-template-columns: 20% 60% 20%;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    /* font-size: 18px; */
    text-align: left;
    margin: 1rem 0;
    padding: 3px 0;
    vertical-align: middle;
    align-items: center;
}
</style>