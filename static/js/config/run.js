productapp.run(["$http", "Authentication", "$location", "$rootScope",
    function ($http, Authentication, $location, $rootScope) {
        $http.defaults.xsrfCookieName = "csrftoken";
        $http.defaults.xsrfHeaderName = "X-CSRFToken";
        if (Authentication.isAuthenticated()) {
            $rootScope.isAuthenticated = Authentication.isAuthenticated();
        } else {
            console.log(Authentication.isAuthenticated());
            $rootScope.isAuthenticated = false;
            $location.url("/home/login");
        }

        $rootScope.$on('$routeChangeSuccess', function(e, current, pre) {
        if(Authentication.isAuthenticated())
        {
          if($location.path()=='/home/login' || $location.path()=='/home/register'){
          $location.url("/home/product");
          }
        }
        else
        {
         if($location.path()!='/home/login' && $location.path()!='/home/register'){
          $location.url("/home/login");
          }
        }

          console.log('Current route name: ' + $location.path());

    });
    }]);