/**
 * Preload — expose only whitelisted APIs when you add IPC.
 */
const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("jobAgent", {
  apiBaseUrl: process.env.APP_API_BASE_URL || "http://127.0.0.1:8000",
});
