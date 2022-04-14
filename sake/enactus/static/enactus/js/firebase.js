// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from "firebase/auth";
import { getDatabase, ref, set, onValue, snapshot } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCyhztJuQz4QNgR3cYkNCAKodHKNT3maC4",
    authDomain: "enactus-sake.firebaseapp.com",
    projectId: "enactus-sake",
    storageBucket: "enactus-sake.appspot.com",
    messagingSenderId: "920466632092",
    appId: "1:920466632092:web:2e73db896459892ccaec59",
    measurementId: "G-6E2KRGTTPV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
console.log(app)


function create_user_account(_email, _password) {
    // `delay` returns a promise
    return new Promise(function (resolve, reject) {

        const auth = getAuth();
        createUserWithEmailAndPassword(auth, _email, _password)
            .then((userCredential) => {
                // Signed in 
                const user = userCredential.user;
                console.log(user)
                // ...
                var uid = user.uid
                console.log("SUCCESS : Account Creation")
                localStorage.setItem("uid", uid)
                resolve(uid)
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                reject(12345)
                // ..
            });

    });
}
$("#btn-signup").click(function () {
    var name = $("#inpt-content-name").text
    var email = $("#inpt-content-email").text
    var password = $("#inpt-content-password").text
    var password_conf = $("#inpt-content-password-conf").text

    if (name != "" && email != "" && password != "" && password_conf != "") {
        create_user_account(email, password)
            .then(function(uid){
                console.log("Created user " + uid);
            })
           .catch(function(flag){
               console.error(flag)
           })
    }

})
