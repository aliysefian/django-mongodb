db.mongotestbase_entrytest.find().count()
db.mongotestbase_entrytest.aggregate([
    {$group:{_id:{status:"$authors.country"},totalPerson:{$sum:1}}}
])
