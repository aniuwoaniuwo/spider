!function(t) {
    if (t.__M = t.__M || {},
    !t.__M.require) {
        var e, n, r = document.getElementsByTagName("head")[0], i = {}, o = {}, a = {}, u = {}, c = {}, s = {}, l = function(t, n) {
            if (!(t in u)) {
                u[t] = !0;
                var i = document.createElement("script");
                if (n) {
                    var o = setTimeout(n, e.timeout);
                    i.onerror = function() {
                        clearTimeout(o),
                        n()
                    }
                    ;
                    var a = function() {
                        clearTimeout(o)
                    };
                    "onload"in i ? i.onload = a : i.onreadystatechange = function() {
                        ("loaded" === this.readyState || "complete" === this.readyState) && a()
                    }
                }
                return i.type = "text/javascript",
                i.src = t,
                r.appendChild(i),
                i
            }
        }, f = function(t, e, n) {
            var r = i[t] || (i[t] = []);
            r.push(e);
            var o, a = c[t] || c[t + ".js"] || {}, u = a.pkg;
            o = u ? s[u].url || s[u].uri : a.url || a.uri || t,
            l(o, n && function() {
                n(t)
            }
            )
        };
        n = function(t, e) {
            "function" != typeof e && (e = arguments[2]),
            t = t.replace(/\.js$/i, ""),
            o[t] = e;
            var n = i[t];
            if (n) {
                for (var r = 0, a = n.length; a > r; r++)
                    n[r]();
                delete i[t]
            }
        }
        ,
        e = function(t) {
            if (t && t.splice)
                return e.async.apply(this, arguments);
            t = e.alias(t);
            var n = a[t];
            if (n)
                return n.exports;
            var r = o[t];
            if (!r)
                throw "[ModJS] Cannot find module `" + t + "`";
            n = a[t] = {
                exports: {}
            };
            var i = "function" == typeof r ? r.apply(n, [e, n.exports, n]) : r;
            return i && (n.exports = i),
            n.exports && !n.exports["default"] && Object.defineProperty && Object.isExtensible(n.exports) && Object.defineProperty(n.exports, "default", {
                value: n.exports
            }),
            n.exports
        }
        ,
        e.async = function(n, r, i) {
            function a(t) {
                for (var n, r = 0, h = t.length; h > r; r++) {
                    var p = e.alias(t[r]);
                    p in o ? (n = c[p] || c[p + ".js"],
                    n && "deps"in n && a(n.deps)) : p in s || (s[p] = !0,
                    l++,
                    f(p, u, i),
                    n = c[p] || c[p + ".js"],
                    n && "deps"in n && a(n.deps))
                }
            }
            function u() {
                if (0 === l--) {
                    for (var i = [], o = 0, a = n.length; a > o; o++)
                        i[o] = e(n[o]);
                    r && r.apply(t, i)
                }
            }
            "string" == typeof n && (n = [n]);
            var s = {}
              , l = 0;
            a(n),
            u()
        }
        ,
        e.resourceMap = function(t) {
            var e, n;
            n = t.res;
            for (e in n)
                n.hasOwnProperty(e) && (c[e] = n[e]);
            n = t.pkg;
            for (e in n)
                n.hasOwnProperty(e) && (s[e] = n[e])
        }
        ,
        e.loadJs = function(t) {
            l(t)
        }
        ,
        e.loadCss = function(t) {
            if (t.content) {
                var e = document.createElement("style");
                e.type = "text/css",
                e.styleSheet ? e.styleSheet.cssText = t.content : e.innerHTML = t.content,
                r.appendChild(e)
            } else if (t.url) {
                var n = document.createElement("link");
                n.href = t.url,
                n.rel = "stylesheet",
                n.type = "text/css",
                r.appendChild(n)
            }
        }
        ,
        e.alias = function(t) {
            return t.replace(/\.js$/i, "")
        }
        ,
        e.timeout = 5e3,
        t.__M.define = n,
        t.__M.require = e
    }
}(this),