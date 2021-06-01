<template>
    <footer class="box-border h-20 lg:h-36 m-0 text-lg text-white bg-green3 flex justify-end align-middle items-center">
        <div class="footerlogo-container marginright inline-flex text-left items-center text-sm lg:text-2xl px-5 mr-auto">
            <img class="logo max-w-10 max-h-10 lg:max-w-20 lg:max-h-20 mr-4" src="../assets/logo.png">
            <p>Rakit PC <br>Impian anda.</p>
        </div>
        <div class="footer-line bg-white overflow-hidden m-0 md:m-5"> </div>
        <div class="footer-extra text-sm lg:text-2xl">
            <p>Tentang Kami</p>
            <p>Persyaratan Layanan (ToS)</p>
        </div> 
    </footer>
</template>

<script>
export default {

}
</script>

<style>
.footer{
    padding:5px 2% ;
    font-family:'Roboto', sans-serif;
    font-weight: 400;
}

.footer-extra p{
    padding: 0;
    margin: 10px;
}

.footer-line{
    width: 1px;
    height: 60%;
    padding: 0;
}
</style>