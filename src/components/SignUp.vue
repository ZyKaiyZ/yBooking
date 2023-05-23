<template>
    <div class="main">
        <div class="first">
            <div id="top">
                <h3 class="header">Welcome to yBooking</h3>
            </div>
            <hr style="width: 100%;">
            <div class="mid">
                <div class="opt">
                    <form>
                        <input type="text" placeholder="Email *" required>
                        <input type="password" placeholder="Password *" required>
                        <input type="password" placeholder="Confirm your Password *" required>
                    </form>
                </div>
                <div class="cbt">
                    <button>Sign Up</button>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
* {
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif;
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
}
.header{
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif; 
    font-size: 55px; 
    color: #222222; 
    font-weight: 600; 
    font-style: normal; 
    line-height: 22px;
    text-align: center;
}
.first {
    border: 3px solid #f53c5e;
    width: 40%;
    padding-left: 30px;
    padding-right: 30px;
    border-radius: 10px;
}
.form {
    width: 95%;
    height: 55px;
    border-radius: 10px 10px 0 0;
}
select {
    font-size: 40px;
    padding-left: 20px;
}
.opt input {
    width: 91%;
    height: 55px;
    border-radius: 10px;
    border: 1px solid gray;
    padding-left: 20px;
    margin: 20px;
    font-size: 30px;
}

::placeholder {
    font-size: 30px;
    padding-left: 10px;

}
.cbt button {
    width: 95%;
    height: 50px;
    margin: 20px;
    background-color: #f53c5e;
    border-radius: 10px;
    color: aliceblue;
    font-size: 30px;
    font-weight: 55px;
    border: none;

}
#text>p {
    font-size: 12px;
    margin-top: 8px;
    margin-bottom: -10px;
    line-height: 16px;
    color: #222222;
    font-weight: 400;
    font-style: normal;
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, "Helvetica Neue", sans-serif;
}
</style>