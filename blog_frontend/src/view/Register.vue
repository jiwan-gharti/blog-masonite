<script setup>

</script>

<template>
        <div class="form_container">
            <h2>Sign Page</h2>
            <div>
                <label for="username">Username</label><br />
                <input id="username" name="username" type="text" />
            </div>
            <div>
                <label for="password">Passowrd</label><br />
                <input id="password" name="password" type="text" />
            </div>
            <div>
                <label for="confirm_password">Confirm Passowrd</label><br />
                <input id="confirm_password" name="confirm_password" type="text" />
            </div>
            <div>
                <input value="Submit" type="submit" />
            </div>
        </div>
</template>


<style scoped>
    .form_container{
        padding: 0.3rem 0;

    }
    .form_container h2{
        color: green;
    }
    .form_container div{
        width: 100%;
    }
    .form_container label{
        font-size: 1.2rem;
        font-weight: 500;
    }
    .form_container input{
        width: 50%;
        margin: 5px 0;
        height: 2rem;
        padding: 0 10px;
        outline: none;
        border-radius: 5px;
    }
    .form_container input[type=submit]{
        width: 5rem;
        font-size: 1rem;
        color: white;
        background-color: green;
        border: none;
        cursor: pointer;
    }
</style>