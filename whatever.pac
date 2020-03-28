function FindProxyForURL(url, host) {
    if (shExpMatch(host, "*.dev")) {
      return "PROXY default.dev";
    }
    return "DIRECT";
  }