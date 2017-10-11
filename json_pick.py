info = {
   "appname":"default",
   "replication":1,
   "nallocated":9,
   "volumename":"test_vol_qVLQt",
   "appid":1,
   "slices":[
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":0,
               "nodeid":3,
               "devid":2,
               "segcnt":28,
               "generation":1,
               "state":"READY"
            },
            {
               "zoneid": 1492539374,
               "leader": 1,
               "sliceidx": 0,
               "nodeid": 3,
               "devid": 2,
               "segcnt": 28,
               "generation": 1,
               "state": "READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":0
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":1,
               "nodeid":1,
               "devid":2,
               "segcnt":32,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":1073741824
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":2,
               "nodeid":1,
               "devid":2,
               "segcnt":29,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":2147483648
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":4,
               "nodeid":2,
               "devid":2,
               "segcnt":32,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":3221225472
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":3,
               "nodeid":2,
               "devid":2,
               "segcnt":25,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":4294967296
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":8,
               "nodeid":2,
               "devid":2,
               "segcnt":17,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":5368709120
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":5,
               "nodeid":3,
               "devid":2,
               "segcnt":1,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":6442450944
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":6,
               "nodeid":1,
               "devid":2,
               "segcnt":1,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":8589934592
      },
      {
         "replicas":[
            {
               "zoneid":1492539374,
               "leader":1,
               "sliceidx":7,
               "nodeid":3,
               "devid":2,
               "segcnt":1,
               "generation":1,
               "state":"READY"
            }
         ],
         "generation":1,
         "state":"READY",
         "loffset":9663676416
      }
   ],
   "volumeid":29,
   "nslices":10
}
node_info = {}

#print(len(info["slices"]))
#print(info["slices"][0]["replicas"][0]["nodeid"])

for s in info["slices"]:

    for r in s["replicas"]:

        print(r["nodeid"])
        k = r["nodeid"]
        print(k)
        if k in node_info:
            node_info[k] += 1
        else:
            node_info[k] = 1

print(node_info)