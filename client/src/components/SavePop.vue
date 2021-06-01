<template>
    <div class="op fixed left-0 right-0 top-0 bottom-0">
        <div class="save-Container text-center top-0 bottom-0 left-0 right-0 fixed m-auto w-5/6 h-3/5 z-50">
            <img @click="ToggleSave()" class="cursor-pointer w-6 lg:w-8 ml-auto mr-1 mt-1" src="../assets/close.svg">
            <p class="text-4xl m-auto xl:text-1xl title text-green1">Save Your Build</p>
            <div class="mx-8 mb-auto mt-12 pt-3 rounded-3xl bg-green3 h-3/5 w-auto">
                <input type="text" placeholder="Type Your Build's Name Here..." class="text-white outline-none inline-block text-base md:text-xl align-middle relative w-5/6 mt-5 px-5 py-4 bg-loginB border-solid border-green1 border-2 rounded-3xl">
                <button @click="$router.push('/Save')" class="save-btn border-none text-black w-5/6 mt-10 px-2 py-4 font-bold text-base md:text-xl text-center inline-block rounded-3xl bg-green1 cursor-pointer">Save</button>
            </div>
        </div>
    </div> 
</template>

<script>
export default {
    props: ['ToggleSave']
}
</script>

<style>
.op{
    background-color: rgb(0, 0, 0, 0.5);
    z-index: 99;
}

.save-Container {
  background-color: #151515;
}

.save-btn:hover{
    background-color: #00B570;
}
</style>