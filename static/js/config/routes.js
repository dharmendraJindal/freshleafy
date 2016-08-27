articlesapp.config(["$routeProvider", "$resourceProvider", "$locationProvider",
    function ($routeProvider, $resourceProvider, $locationProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;
        $routeProvider
            .when("/", {
                templateUrl: "/static/partials/articles/ListOfAllArticles.html",
                controller: "ListOfAllArticleController"
            })
            .when("/login", {
                controller: "LoginController",
                templateUrl: "/static/partials/authentication/login.html"
            })
            .when("/register", {
                controller: "RegisterController",
                templateUrl: "/static/partials/authentication/register.html"
            })
            .when("/article/add", {
                controller: "NewArticleController",
                templateUrl: "/static/partials/articles/forms/CreateArticleForm.html"
            })
            .when("/article/edit/:id", {
                controller: "EditArticleController",
                templateUrl: "/static/partials/articles/forms/ArticleEditForm.html"
            })
            .when("/article/:id", {
                controller: "SingleArticleController",
                templateUrl: "/static/partials/articles/SingleArticle.html"
            })
            .when("/inline", {
                controller: "InlineEditController",
                templateUrl: "/static/partials/articles/InlineEdit.html"
            })
            .when("/upload", {
                controller: "FileUploadController",
                templateUrl: "/static/partials/file_upload/file_upload.html"
            })
            .otherwise({
                redirectTo: '/'
            });

        $locationProvider.html5Mode(true);
    }
]);