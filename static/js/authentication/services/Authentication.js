productapp.factory("Authentication", ["$cookies", "$http","$q", "$rootScope", function ($cookies, $http,$q, $rootScope) {
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

    function login(loginParams) {
      var deferred=$q.defer();
        $http.post("/api/v1/auth/login/", {
            username: loginParams.username, password: loginParams.password
        }).then(loginSuccessFn, loginErrorFn);

        function loginSuccessFn(data) {
            Authentication.setAuthenticatedAccount(data.data);
            window.location = "/";
            deferred.resolve();
        }

        function loginErrorFn(status) {
        deferred.reject();
           // console.error("Epic failure! with error code");
        }
        return deferred.promise;
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

    function register(registerParams) {
    var deferred=$q.defer();
         $http.post("/api/v1/auth/register/", {
            first_name: registerParams.firstName,
            last_name: registerParams.lastName,
            company: registerParams.companyName,
            email: registerParams.email,
            password: registerParams.password,
            phonenumber: registerParams.phone_number
        }).then(registerSuccessFn, registerErrorFn);

        function registerSuccessFn(data) {
            deferred.resolve();
        }

        function registerErrorFn(status) {
        deferred.reject();
        }
        return deferred.promise;
    }

    function setAuthenticatedAccount(account) {
        $cookies.put("authenticatedAccount", JSON.stringify(account));
    }

    function unauthenticate() {
        $cookies.remove("authenticatedAccount");
    }
}]);
