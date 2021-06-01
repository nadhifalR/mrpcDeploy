<template>
    <div class="op fixed left-0 right-0 top-0 bottom-0">
        <div class="market-Container text-white top-0 bottom-0 left-0 right-0 fixed m-auto w-5/6 h-4/5 z-50">
            <img @click="TogglePopup()" class="cursor-pointer w-6 lg:w-8 ml-auto mr-1 mt-1" src="../assets/close.svg">
            <p class="text-4xl mb-4 ml-8 xl:text-1xl title">Find your part here</p>
            <div class="market-List left-0 right-0 mx-8 mb-auto mt-8 pt-3 rounded-3xl bg-green3 h-3/4 w-auto">
                <p class="ml-4 text-lg title">Nama_Part</p>
                <div class="line mx-4 w-auto h-px bg-green1 my-3 overflow-hidden"></div>
                
                <div class="market-List-Container flex flex-wrap justify-center" >
                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market1.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">Bukalapak</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market2.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">JD.ID</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market3.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">Lazada</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market4.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">Shopee</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market5.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">Blibli.com</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    <div class="market-card rounded-2xl bg-black w-32 h-28 md:w-40 md:h-32 lg:w-60 lg:h-36 mx-2 my-1 overflow-hidden text-center">
                        <div class="market-card-img  bg-white rounded-t-2xl h-16 lg:h-20 overflow-hidden">
                            <img class=" left-0 right-0 top-0 bottom-0 mt-6 mx-auto w-28 " src="../assets/market6.png">
                        </div>
                        <p class="market-name-Title font-medium text-black text-sm bg-white">Tokopedia</p>
            
                        <div class="market-buy text-xs text-white flex justify-center align-middle">
                            <button class="beli-btn mt-1 lg:mt-3 lg:mx-20">Beli Sekarang</button>
                        </div>
                    </div>

                    
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
export default {
    props: ['TogglePopup']
}
</script>

<style>
.op{
    background-color: rgb(0, 0, 0, 0.5);
    z-index: 99;
}

.market-Container {
  background-color: #151515;
}

.beli-btn{
    border: none;
    color: black;
    width: 100%;
    height: 70%;
    background-color: #02F39B;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    cursor: pointer;
    /* font-size: 20px; */
}
</style>