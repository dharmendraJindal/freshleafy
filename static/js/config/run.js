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

        $rootScope.$on('$routeChangeSuccess', function(e, current, pre) {
        if(Authentication.isAuthenticated())
        {
          if($location.path()=='/login' || $location.path()=='/register'){
          $location.url("/product");
          }
        }
        else
        {
         if($location.path()!='/login' && $location.path()!='/register'){
          $location.url("/login");
          }
        }
          console.log('Current route name: ' + $location.path());

    });
    }]);