articlesapp.factory("Authentication", ["$cookies", "$http", function ($cookies, $http) {
    var Authentication = {
        getAuthenticatedAccount: getAuthenticatedAccount,
        isAuthenticated: isAuthenticated,
        login: login,
        logout: logout,
        register: register,
        setAuthenticatedAccount: setAuthenticatedAccount,
        unauthenticate: unauthenticate
    };

    return Authentication;

    function getAuthenticatedAccount() {
        if (!$cookies.get("authenticatedAccount")) {
            return;
        }
        return JSON.parse($cookies.get("authenticatedAccount"));
    }

    function isAuthenticated() {
        return !!$cookies.get("authenticatedAccount");
    }

    function login(username, password) {
        return $http.post("/api/v1/auth/login/", {
            username: username, password: password
        }).then(loginSuccessFn, loginErrorFn);

        function loginSuccessFn(data) {
            Authentication.setAuthenticatedAccount(data.data);
            window.location = "/";
        }

        function loginErrorFn(status) {
            console.error("Epic failure! with error code" + status);
        }
    }

    function logout() {
        return $http.get("/api/v1/auth/logout/")
            .then(logoutSuccessFn, logoutErrorFn);

        function logoutSuccessFn(status) {
            Authentication.unauthenticate();
            window.location = "/";
        }

        function logoutErrorFn(status) {
            console.error("Epic failure! with status" + status);
        }
    }

    function register(email, password, username) {
        return $http.post("/api/v1/auth/register/", {
            username: username,
            password: password,
            email: email
        }).then(registerSuccessFn, registerErrorFn);

        function registerSuccessFn(data) {
            Authentication.login(data.data.username, data.data.password);
        }

        function registerErrorFn(status) {
            console.error("Epic failure! with status" + status);
        }
    }

    function setAuthenticatedAccount(account) {
        $cookies.put("authenticatedAccount", JSON.stringify(account));
    }

    function unauthenticate() {
        $cookies.remove("authenticatedAccount");
    }
}]);
