productapp.run(["$http", "Authentication", "$location", "$rootScope",
    function ($http, Authentication, $location, $rootScope) {
        $http.defaults.xsrfCookieName = "csrftoken";
        $http.defaults.xsrfHeaderName = "X-CSRFToken";
        if (Authentication.isAuthenticated()) {
            $rootScope.isAuthenticated = Authentication.isAuthenticated();
        } else {
            console.log(Authentication.isAuthenticated());
            $rootScope.isAuthenticated = false;
            $location.url("/login");
        }
    }]);