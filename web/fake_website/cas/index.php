<!DOCTYPE html><html>

<head>
    <meta charset="UTF-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" /><title>bxinp Connexion</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
        <link rel="stylesheet" type="text/css" href="/assets/normalize.css" /><link rel="stylesheet" type="text/css" href="/assets/bootstrap-grid.min.css" /><link rel="stylesheet" type="text/css" href="/assets/material-components-web.min.css" /><link rel="stylesheet" type="text/css" href="/assets/materialdesignicons.min.css" /><link rel="stylesheet" type="text/css" href="/assets/cas.css" /><link rel="shortcut icon"
        href="/assets/favicon.ico" /></head>

<body class="login mdc-typography">
    <script type="text/javascript" src="/js/jquery.min.js"></script>
<script type="text/javascript" src="/js/es5-shim.min.js"></script>
    <script type="text/javascript" src="/js/css-vars-ponyfill.min.js"></script>
    <script type="text/javascript" src="/js/material-components-web.min.js"></script>
<script type="text/javascript" src="/js/cas.js"></script>
<script type="text/javascript" src="/js/material.js"></script>
<script>
    if (typeof resourceLoadedSuccessfully === "function") {
        resourceLoadedSuccessfully();
    }
    $(function() {
        typeof cssVars === "function" && cssVars({onlyLegacy: true});
    })
</script>

<script>
    /*<![CDATA[*/

    var trackGeoLocation = false;

    var googleAnalyticsTrackingId = null;

    if (googleAnalyticsTrackingId != null && googleAnalyticsTrackingId != '') {
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r;
            i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date();
            a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
            a.async = 1;
            a.src = g;
            m.parentNode.insertBefore(a, m)
        })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

        ga('create', googleAnalyticsTrackingId, 'auto');
        ga('send', 'pageview');
    }

    /*]]>*/
</script>
<div>

    <header id="app-bar" class="mdc-top-app-bar mdc-top-app-bar--fixed mdc-elevation--z4 shadow-sm">
        <nav class="mdc-top-app-bar__row navbar navbar-dark bg-dark">
            <div class="container-fluid container-fluid d-flex align-items-center justify-content-between">
                <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
                    </section>
                <section class="mdc-top-app-bar__section">
                    <span class="cas-brand mx-auto">
                        <span class="visually-hidden">bxinp</span>
                        <img id="cas-logo" class="cas-logo"
                            title="bxinp"
                            src="/assets/logo.bxinp.png"
                            /></span>
                </section>
                <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end">
                    <!--                <a id="cas-user-account"--><!--                   th:href="@{/account}"--><!--                   th:if="${ticketGrantingTicketId != null}"--><!--                   class="mdc-icon-button mdc-top-app-bar__action-item"--><!--                   aria-label="User Account">--><!--                    <span class="mdi mdi-account-group"></span>--><!--                    <span class="visually-hidden">user account</span>--><!--                </a>--></section>
            </div>
        </nav>
    </header>
    <script>var countMessages = 0;</script>
    <script type="text/javascript">

        (function (material) {
            var header = {
                init: function () {
                    header.attachTopbar();
                    material.autoInit();
                },
                attachDrawer: function () {
                    var elm = document.getElementById('app-drawer');
                    if (elm != null) {
                        var drawer = material.drawer.MDCDrawer.attachTo(elm);
                        var closeDrawer = function (evt) {
                            drawer.open = false;
                        };
                        drawer.foundation.handleScrimClick = closeDrawer;
                        document.onkeydown = function (evt) {
                            evt = evt || window.event;
                            if (evt.keyCode == 27) {
                                closeDrawer();
                            }
                        };
                        header.drawer = drawer;
                        return drawer;
                    }
                    return undefined;
                },
                attachTopbar: function (drawer) {

                    var drawer = header.attachDrawer();
                    var dialog = header.attachNotificationDialog();

                    if (drawer != undefined) {
                        header.attachDrawerToggle(drawer);
                    }
                    if (dialog != undefined) {
                        header.attachNotificationToggle(dialog);
                    }
                },
                checkCaps: function (ev) {
                    var s = String.fromCharCode(ev.which);
                    if (s.toUpperCase() === s && s.toLowerCase() !== s && !ev.shiftKey) {
                        ev.target.parentElement.classList.add('caps-on');
                    } else {
                        ev.target.parentElement.classList.remove('caps-on');
                    }
                },
                attachDrawerToggle: function (drawer) {
                    let appBar = document.getElementById('app-bar');
                    if (appBar != null) {
                        let topAppBar = material.topAppBar.MDCTopAppBar.attachTo(appBar);
                        topAppBar.setScrollTarget(document.getElementById('main-content'));
                        topAppBar.listen('MDCTopAppBar:nav', function () {
                            drawer.open = !drawer.open;
                        });
                        return topAppBar;
                    }
                    return undefined;
                },
                attachNotificationDialog: function () {
                    var element = document.getElementById('cas-notification-dialog');
                    if (element != null) {
                        return material.dialog.MDCDialog.attachTo(element);
                    }
                    return undefined;
                },
                attachNotificationToggle: function (dialog) {
                    var btn = document.getElementById('cas-notifications-menu');
                    if (btn != null) {
                        btn.addEventListener('click', function () {
                            dialog.open();
                        });
                    }
                }
            }
            document.addEventListener('DOMContentLoaded', function () {
                if (material) {
                    header.init();
                }
                if (countMessages == 0) {
                    window.jQuery('#notifications-count').remove();
                } else {
                    window.jQuery('#notifications-count').text("(" + countMessages + ")")
                }
            });
        })(typeof mdc !== 'undefined' && mdc);
    </script>
</div>

    <div class="mdc-drawer-scrim"></div>

    <div class="mdc-drawer-app-content mdc-top-app-bar--fixed-adjust d-flex justify-content-center">
        <main role="main" id="main-content" class="container-lg py-4">
            <div id="content" class="d-flex justify-content-center">
   <div class="d-flex justify-content-center flex-md-row flex-column mdc-card mdc-card-content card flex-grow-1">
        <section id="loginForm"
                 class="login-section login-form card-body">
            <div class="d-flex flex-column justify-content-between m-auto">

        <div>
            </div>

        <div class="form-wrapper">

            <form method="post" id="fm1" action="login.php">
                <div id="login-form-controls">
                    <h3 class="text-center">
                        <i class="mdi mdi-security fas fa-shield-alt"></i>
                        <span>Entrez votre identifiant et votre mot de passe.</span>
                    </h3>

                    <section class="cas-field form-group my-3" id="usernameSection">
                        <label for="username"
                               class="mdc-text-field mdc-text-field--outlined control-label w-100">
                            <span class="mdc-notched-outline">
                                <span class="mdc-notched-outline__leading"></span>
                                <span class="mdc-notched-outline__notch">
                                    <span class="mdc-floating-label"><span class="accesskey">I</span>dentifiant (login) :</span>
                                </span>
                                <span class="mdc-notched-outline__trailing"></span>
                            </span>
                            <input class="mdc-text-field__input form-control" id="username"
                                   size="25"
                                   type="text"
                                   accesskey="i"
                                   autocapitalize="none"
                                   spellcheck="false"
                                   autocomplete="username" required name="username" value=""/></label>

                        <div class="mdc-text-field-helper-line">
                            <div class="mdc-text-field-helper-text mdc-text-field-helper-text--validation-msg" aria-hidden="true">
                                <span id="usernameValidationMessage">Vous devez entrer votre identifiant.</span>
                            </div>
                        </div>

                        <script type="text/javascript">
                            /*<![CDATA[*/
                            var username = "";
                            var disabled = false;

                            if (username != null && username !== '') {
                                $('#username').val(username);
                                if (disabled) {
                                    $('#usernameSection').hide();
                                }
                            }
                            /*]]>*/
                        </script>
                    </section>
                    <section class="cas-field form-group my-3 mdc-input-group form-group" id="passwordSection">
                        <div class="mdc-input-group-field mdc-input-group-field-append">
                            <div class="caps-check">
                                <label for="password"
                                       class="mdc-text-field caps-check mdc-text-field--outlined control-label mdc-text-field--with-trailing-icon control-label w-100">
                                    <span class="mdc-notched-outline">
                                        <span class="mdc-notched-outline__leading"></span>
                                        <span class="mdc-notched-outline__notch">
                                            <span class="mdc-floating-label"><span class="accesskey">M</span>ot de passe :</span>
                                        </span>
                                        <span class="mdc-notched-outline__trailing"></span>
                                    </span>
                                    <input class="mdc-text-field__input form-control pwd"
                                           type="password"
                                           id="password"
                                           size="25"
                                           required
                                           accesskey="m"
                                           autocomplete="off" name="password" value=""/><button
                                            class="reveal-password align-self-end mdc-button mdc-button--unelevated mdc-input-group-append mdc-icon-button btn btn-primary"
                                            tabindex="-1" type="button">
                                        <i class="mdi mdi-eye reveal-password-icon fas fa-eye"></i>
                                        <span class="visually-hidden">Toggle Password</span>
                                    </button>
                                </label>
                                <div class="mdc-text-field-helper-line">
                                    <div
                                            class="mdc-text-field-helper-text mdc-text-field-helper-text--validation-msg"
                                            aria-hidden="true">
                                        <span id="passwordValidationMessage">Vous devez entrer votre mot de passe.</span>
                                    </div>
                                </div>
                                <div class="mdc-text-field-helper-line caps-warn">
                                    <div
                                            class="mdc-text-field-helper-text mdc-text-field-helper-text--persistent mdc-text-field-helper-text--validation-msg text-danger">
                                        <span>La touche Verr Maj est activée !</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section class="cas-field form-group my-3">
                        </section>


                    <section class="cas-field">

                        <input type="hidden" name="execution" value="7665e785-9d2e-46ff-8d7d-12376e0c9408_ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LkNWU19RdWZJM09PRXU3VE1qRkYxZGNKbUhTZWJEbFQ3NzlteWZxdXJ6bjg2QjFnZWJ3S1c3Wl9SemVGLXlGZHIxWUhhOUJfc3prN0RmVE4zbXVrQ2NnLUYtc3pHYzUzemhmU3hjbnRCOEl4N1NnckpEdkN6TjRwWXFFcUd3dnNoQU1FX05ORHkxNTFOWjhjNnN0NnI4cENGVUhOWklSbHlTTW9qSW1yeGhXUVg5Tmt1cjNja1hldW9uOTdpYmtobFhwaGcyWWYwUzl4RjlGNVNsY1h3VFNSbzlWZ1NIaUVVRUFTMGVHOW5xU2xJc0tPS1BGQkdKR0s1ZEtJSlpnb0t5SENMLTl0dEJHbzJrTUJ1djIzSUQ1YlpqNVFCa2FlWGNsTlJlRUEyOGFzWWJLa3Q0Y1RjaWhtRzlodVYxNFA0RXRpMVF2RGYwLUkxVmExblotMF9ORzcwQzRqeDE3TzBrS2xQTHp3QXlqb1lFZW1VZ1ZVb1k3aVdVT1hxV2IzeU1La2xlWXJrUDN0S3VIdmVRSVVmWElEMkZiMWpQNFVVbk9adFhTS3ltT1FTTG45T2RmUldwbEVUMzZpSFZENFpaM0YwdXgxbjJDM25EQ3IwcGJWTEFUZTlEeWY1ang5dE81bTVxSGUtQWJJMVYtWmlTSEdrNVdlRzREbmRWQ3o4emlmRVhVWVhFczZLSnE4VWo2bnRwVEdMdjRmLVFzYXhBWTdyWkFPdXlvRjRLSV9Mb3haNnBIUWtnLVRMc2FnSVlIck4zUEVSR0p1WS10Z2tUS3pRdURNQ3ZHdDhTV2NNd1FCMGdFeUZSR09zU3k5X21FNnZIelFuR3Bub1BQOHZXMTJ6UHpka0lVTnBpX29fZmdHM3hHVFp4a1U4T3JKZzAzZHloM2RZa3Z0RVBiX2d1QWZIX2tqY3BfZUFoRjBpNUhDeG1aaEYzeTNZeG5DS1hUaHFfNEFjYm5xNjhRcDlnZ1NVQ2dfa2dCTkpPdWExVWFuUWNvLWQ5b0ZHNmxIS1U0RW5VT3BOa3RHZTN0YmFTVVEyUy1XbnFPX0RiTURNYm5NbFZWWENIRnN6MjctaFlWWjZrV2p0aG0wdjNlMV9XZENvcThUeDNvZ2Z1aXd4ZTZ2NnF4WE1pcUZaUUpwMTJUbWQtQmFJaTh0Y3VacVA4TngyRk1PZlVWRXl0RTM1RkplR3gzd3J5TG9BODFGSFV5UG5Jc1lpVlRNbmpYekpELUpadGFGZG9tNFNGNlcydnI0ODd0T0xkWTFqamFXaUNaZUZFUG1FZFdwTTNLeWhzX190VDNXRjVlOFNmeGswTmZQd1pSb2tKT0xoY19aNEtIcnBaOGstSmlXd0EwMDhfTGNvZUp3S25iZlVvb1Z1Z1JySVFpeUZTZXQtaF9yemc0U2JJR0RFX1JqUGJfcHRvT0pJMjVEVWJ1ejguZW9uUGJ5am1uQ1RqeWV0WDEyNDV5WTFLcFZMbUc2VWxTTjl1RW9Bc1VvejkwR2V3cGYtdkdLNmpmcXpIajVCR3hBbTVNNHlfVnlmcW13a0lpWE5oZGc="/><input type="hidden" name="_eventId" value="submit"/><input type="hidden" name="geolocation"/></section>

                    <button
                class="mdc-button mdc-button--raised btn btn-primary btn-primary"
                name="submit"
                accesskey="l"
                type="submit">
            <span class="mdc-button__label">SE CONNECTER</span>
        </button>

        </div>
            </form>

            <hr class="my-4"/><span>
                    <div id="pmlinks" class="my-2">
        </div>
                </span>

            <script type="text/javascript">
                /*<![CDATA[*/
                var i = "Veuillez patienter..."
                var j = "SE CONNECTER"
                    /*]]>*/
                    $(window).on('pageshow', function () {
                        $(':submit').prop('disabled', false);
                        $(':submit').attr('value', j);
                    });
                $(document).ready(function () {
                    $("#fm1").submit(function () {
                        $(":submit").attr("disabled", true);
                        $(":submit").attr("value", i);
                        return true;
                    });
                });
            </script>
        </div>

        <span>
            <div id="sidebar">
            <div class="sidebar-content">
                <p>Pour des raisons de sécurité, veuillez vous <a href="logout">déconnecter</a> et fermer votre navigateur lorsque vous avez fini d'accéder aux services authentifiés.</p>
            </div>
        </div>
        </span>

    </div>
        </section>
        <span>
            </span>
        </div>
</div>
        </main>
    </div>

    <footer class="py-4 d-flex justify-content-center align-items-center cas-footer">
    <span id="copyright" class="me-2 d-inline-block">Copyright &copy; 2005&ndash;2021 Apereo, Inc.</span>
    <span class="px-3 d-inline-block">Powered by <a href="https://github.com/apereo/cas">Apereo CAS</a></span>
</footer>

</body>

</html>