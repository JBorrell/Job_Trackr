from flask.ext.restful import Resource, fields, marshal, reqparse
from server import db
from server.models.job import Job

company_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

job_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'company': fields.Nested(company_fields),
    'salary': fields.Integer,
    'location': fields.String,
    'summary': fields.String,
    'perks': fields.String

}


class JobsResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', location='json')
        self.reqparse.add_argument('salary', location='json')
        self.reqparse.add_argument('location', location='json')
        self.reqparse.add_argument('summary', location='json')
        self.reqparse.add_argument('perks', location='json')
        super().__init__()


class JobsAPI(JobsResource):
    def post(self, company_id):
        args = self.reqparse.parse_args()
        args['company_id'] = company_id
        job = Job(args)
        db.session.add(job)
        db.session.commit()
        return 'Job Created!', 201


class JobAPI(JobsResource):
    def get(self, company_id, id):
        job = Job.query.get(id)
        return marshal(job, job_fields)

    def put(self, company_id, id):
        args = self.reqparse.parse_args()
        args['company_id'] = company_id
        job = Job.query.filter_by(id=id)
        job.update(args)
        db.session.commit()
        return marshal(job[0], job_fields)

    def delete(self, company_id, id):
        job = Job.query.get(id)
        db.session.delete(job)
        db.session.commit()
        return '', 204
